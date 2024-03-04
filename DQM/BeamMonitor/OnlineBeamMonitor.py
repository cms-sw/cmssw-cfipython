import FWCore.ParameterSet.Config as cms

def OnlineBeamMonitor(**kwargs):
  mod = cms.EDProducer('OnlineBeamMonitor',
    MonitorName = cms.untracked.string('YourSubsystemName'),
    AppendRunToFileName = cms.untracked.bool(False),
    WriteDIPAscii = cms.untracked.bool(True),
    DIPFileName = cms.untracked.string('BeamFitResultsForDIP.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
