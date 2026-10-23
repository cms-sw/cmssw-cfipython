import FWCore.ParameterSet.Config as cms

def StripCompactDigiSimLinksProducer(*args, **kwargs):
  mod = cms.EDProducer('StripCompactDigiSimLinksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
