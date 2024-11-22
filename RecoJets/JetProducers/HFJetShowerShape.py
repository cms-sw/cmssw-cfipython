import FWCore.ParameterSet.Config as cms

def HFJetShowerShape(*args, **kwargs):
  mod = cms.EDProducer('HFJetShowerShape',
    jets = cms.InputTag('ak4PFJetsCHS'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    jetPtThreshold = cms.double(25),
    jetEtaThreshold = cms.double(2.9),
    hfTowerEtaWidth = cms.double(0.175),
    hfTowerPhiWidth = cms.double(0.175),
    vertexRecoEffcy = cms.double(0.7),
    offsetPerPU = cms.double(0.4),
    jetReferenceRadius = cms.double(0.4),
    stripPtThreshold = cms.double(10),
    widthPtThreshold = cms.double(3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
