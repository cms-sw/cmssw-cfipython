import FWCore.ParameterSet.Config as cms

def PFDisplacedVertexProducer(**kwargs):
  mod = cms.EDProducer('PFDisplacedVertexProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
