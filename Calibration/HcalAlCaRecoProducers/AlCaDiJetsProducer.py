import FWCore.ParameterSet.Config as cms

def AlCaDiJetsProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
