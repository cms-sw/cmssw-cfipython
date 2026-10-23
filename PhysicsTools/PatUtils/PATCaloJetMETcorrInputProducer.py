import FWCore.ParameterSet.Config as cms

def PATCaloJetMETcorrInputProducer(*args, **kwargs):
  mod = cms.EDProducer('PATCaloJetMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
