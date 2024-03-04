import FWCore.ParameterSet.Config as cms

def TrackFromPVSelector(**kwargs):
  mod = cms.EDProducer('TrackFromPVSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
