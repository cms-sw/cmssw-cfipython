import FWCore.ParameterSet.Config as cms

def OnlineBeamMonitor(*args, **kwargs):
  mod = cms.EDProducer('OnlineBeamMonitor',
    MonitorName = cms.untracked.string('YourSubsystemName'),
    AppendRunToFileName = cms.untracked.bool(False),
    WriteDIPAscii = cms.untracked.bool(True),
    DIPFileName = cms.untracked.string('BeamFitResultsForDIP.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
