import FWCore.ParameterSet.Config as cms

def DTChamberMasker(**kwargs):
  mod = cms.EDProducer('DTChamberMasker',
    digiTag = cms.InputTag('simMuonDTDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
