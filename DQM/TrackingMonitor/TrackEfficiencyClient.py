import FWCore.ParameterSet.Config as cms

def TrackEfficiencyClient(*args, **kwargs):
  mod = cms.EDProducer('TrackEfficiencyClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
