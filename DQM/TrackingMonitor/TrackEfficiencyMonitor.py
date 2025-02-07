import FWCore.ParameterSet.Config as cms

def TrackEfficiencyMonitor(*args, **kwargs):
  mod = cms.EDProducer('TrackEfficiencyMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
