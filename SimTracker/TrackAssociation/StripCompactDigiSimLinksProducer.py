import FWCore.ParameterSet.Config as cms

def StripCompactDigiSimLinksProducer(**kwargs):
  mod = cms.EDProducer('StripCompactDigiSimLinksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
