# batch_runner_with_progress.ps1

# Define parameter ranges
$range1 = 20..0
$range2 = 0..20
$range3 = 0..20

# Calculate the total number of combinations
$totalTasks = $range1.Count * $range2.Count * $range3.Count
$completedTasks = 0

# Iterate over parameter combinations
foreach ($i in $range1) {
    foreach ($j in $range2) {
        foreach ($k in $range3) {
            # Start a background job
            Start-Job -ScriptBlock {
                param($a, $b, $c)
                python C:\Users\happp\Documents\2024_ScienceFair_Mirror\Script\_Blank_Experiments.py $a $b $c
            } -ArgumentList $k, $j, $i

            # Increment completed task count and update progress
            $completedTasks++
            $percentComplete = [math]::Round(($completedTasks / $totalTasks) * 100, 2)

            # Update progress bar
            Write-Progress -Activity "Running batch tasks" `
                            -Status "$percentComplete% complete" `
                            -PercentComplete $percentComplete

            # Limit the number of concurrent jobs
            while ((Get-Job -State Running).Count -ge 12) {
                Start-Sleep -Milliseconds 500
            }
        }
    }
}

# Wait for all jobs to finish
Get-Job | Wait-Job

# Cleanup completed jobs
Get-Job | Remove-Job

# Final message
Write-Host "All tasks completed successfully!"
