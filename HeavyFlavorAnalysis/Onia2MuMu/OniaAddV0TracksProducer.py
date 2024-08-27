import FWCore.ParameterSet.Config as cms

def OniaAddV0TracksProducer(**kwargs):
  mod = cms.EDProducer('OniaAddV0TracksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
