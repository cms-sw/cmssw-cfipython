import FWCore.ParameterSet.Config as cms

def EtaEtMinCaloJetCountFilter(**kwargs):
  mod = cms.EDFilter('EtaEtMinCaloJetCountFilter',
    src = cms.InputTag(''),
    etMin = cms.double(0),
    etaMin = cms.double(0),
    etaMax = cms.double(0),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
