import FWCore.ParameterSet.Config as cms

def SoftLepton(**kwargs):
  mod = cms.EDProducer('SoftLepton',
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag('muons'),
    primaryVertex = cms.InputTag('offlinePrimaryVertices'),
    leptonCands = cms.InputTag(''),
    leptonId = cms.InputTag(''),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag('ak4PFJetsCHS'),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
