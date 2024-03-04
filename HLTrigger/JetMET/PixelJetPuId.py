import FWCore.ParameterSet.Config as cms

def PixelJetPuId(**kwargs):
  mod = cms.EDProducer('PixelJetPuId',
    jets = cms.InputTag('hltCaloJetL1FastJetCorrected'),
    tracks = cms.InputTag('hltPixelTracksNoPU'),
    primaryVertex = cms.InputTag('hltFastPVPixelVertices'),
    MinGoodJetTrackPtRatio = cms.double(0.045),
    MinGoodJetTrackPt = cms.double(1.8),
    MaxTrackDistanceToJet = cms.double(0.04),
    MinTrackPt = cms.double(0.6),
    MaxTrackChi2 = cms.double(20),
    UseForwardJetsAsNoPU = cms.bool(True),
    MinEtaForwardJets = cms.double(2.4),
    MinEtForwardJets = cms.double(40),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
