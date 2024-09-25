import FWCore.ParameterSet.Config as cms

def ME0ChamberMasker(*args, **kwargs):
  mod = cms.EDProducer('ME0ChamberMasker',
    digiTag = cms.InputTag('simMuonME0Digis'),
    me0Minus = cms.bool(True),
    me0Plus = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
