import FWCore.ParameterSet.Config as cms

def HLTScoutingCaloProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTScoutingCaloProducer',
    caloJetCollection = cms.InputTag('hltAK4CaloJets'),
    caloJetBTagCollection = cms.InputTag('hltCombinedSecondaryVertexBJetTagsCalo'),
    caloJetIDTagCollection = cms.InputTag('hltCaloJetFromPV'),
    vertexCollection = cms.InputTag('hltPixelVertices'),
    metCollection = cms.InputTag('hltMet'),
    rho = cms.InputTag('hltFixedGridRhoFastjetAllCalo'),
    caloJetPtCut = cms.double(20),
    caloJetEtaCut = cms.double(3),
    doMet = cms.bool(True),
    doJetBTags = cms.bool(False),
    doJetIDTags = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
