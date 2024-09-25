import FWCore.ParameterSet.Config as cms

def DTChamberMasker(*args, **kwargs):
  mod = cms.EDProducer('DTChamberMasker',
    digiTag = cms.InputTag('simMuonDTDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
