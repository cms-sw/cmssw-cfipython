import FWCore.ParameterSet.Config as cms

def TrackEfficiencyMonitor(**kwargs):
  mod = cms.EDProducer('TrackEfficiencyMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
