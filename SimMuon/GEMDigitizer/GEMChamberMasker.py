import FWCore.ParameterSet.Config as cms

def GEMChamberMasker(*args, **kwargs):
  mod = cms.EDProducer('GEMChamberMasker',
    digiTag = cms.InputTag('simMuonGEMDigis'),
    ge11Minus = cms.bool(True),
    ge11Plus = cms.bool(True),
    ge21Minus = cms.bool(True),
    ge21Plus = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
