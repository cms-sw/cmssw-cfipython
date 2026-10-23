import FWCore.ParameterSet.Config as cms

def EleIdCutBasedExtProducer(*args, **kwargs):
  mod = cms.EDProducer('EleIdCutBasedExtProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
