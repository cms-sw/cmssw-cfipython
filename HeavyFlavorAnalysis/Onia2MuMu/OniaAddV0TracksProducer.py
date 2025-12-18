import FWCore.ParameterSet.Config as cms

def OniaAddV0TracksProducer(*args, **kwargs):
  mod = cms.EDProducer('OniaAddV0TracksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
