import FWCore.ParameterSet.Config as cms

def AlCaDiJetsProducer(**kwargs):
  mod = cms.EDProducer('AlCaDiJetsProducer',
    PFjetInput = cms.InputTag('ak4PFJetsCHS'),
    HBHEInput = cms.InputTag('hbhereco'),
    HFInput = cms.InputTag('hfreco'),
    HOInput = cms.InputTag('horeco'),
    particleFlowInput = cms.InputTag('particleFlow'),
    VertexInput = cms.InputTag('offlinePrimaryVertices'),
    MinPtJet = cms.double(20),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
