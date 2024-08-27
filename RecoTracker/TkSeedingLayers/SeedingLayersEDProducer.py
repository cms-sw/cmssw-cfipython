import FWCore.ParameterSet.Config as cms

def SeedingLayersEDProducer(**kwargs):
  mod = cms.EDProducer('SeedingLayersEDProducer',
    layerList = cms.vstring(),
    BPix = cms.PSet(),
    FPix = cms.PSet(),
    TIB = cms.PSet(),
    TID = cms.PSet(),
    TOB = cms.PSet(),
    TEC = cms.PSet(),
    MTIB = cms.PSet(),
    MTID = cms.PSet(),
    MTOB = cms.PSet(),
    MTEC = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
