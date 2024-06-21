import FWCore.ParameterSet.Config as cms

def PFConversionProducer(**kwargs):
  mod = cms.EDProducer('PFConversionProducer',
    conversionCollection = cms.InputTag('allConversions'),
    PrimaryVertexLabel = cms.InputTag('offlinePrimaryVertices'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
