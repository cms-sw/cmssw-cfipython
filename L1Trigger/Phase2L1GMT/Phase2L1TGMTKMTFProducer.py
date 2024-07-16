import FWCore.ParameterSet.Config as cms

def Phase2L1TGMTKMTFProducer(**kwargs):
  mod = cms.EDProducer('Phase2L1TGMTKMTFProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
