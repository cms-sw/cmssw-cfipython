import FWCore.ParameterSet.Config as cms

def MuPFIsoEmbedder(**kwargs):
  mod = cms.EDProducer('MuPFIsoEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
