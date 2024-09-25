import FWCore.ParameterSet.Config as cms

def PFConversionProducer(*args, **kwargs):
  mod = cms.EDProducer('PFConversionProducer',
    conversionCollection = cms.InputTag('allConversions'),
    PrimaryVertexLabel = cms.InputTag('offlinePrimaryVertices'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
