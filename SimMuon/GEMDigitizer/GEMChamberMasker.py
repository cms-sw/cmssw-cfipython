import FWCore.ParameterSet.Config as cms

def GEMChamberMasker(**kwargs):
  mod = cms.EDProducer('GEMChamberMasker',
    digiTag = cms.InputTag('simMuonGEMDigis'),
    ge11Minus = cms.bool(True),
    ge11Plus = cms.bool(True),
    ge21Minus = cms.bool(True),
    ge21Plus = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
