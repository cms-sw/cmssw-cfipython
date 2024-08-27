import FWCore.ParameterSet.Config as cms

def ME0ChamberMasker(**kwargs):
  mod = cms.EDProducer('ME0ChamberMasker',
    digiTag = cms.InputTag('simMuonME0Digis'),
    me0Minus = cms.bool(True),
    me0Plus = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
