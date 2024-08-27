import FWCore.ParameterSet.Config as cms

def IsolatedPixelTrackCandidateProducer(**kwargs):
  mod = cms.EDProducer('IsolatedPixelTrackCandidateProducer',
    L1eTauJetsSource = cms.InputTag('hltCaloStage2Digis', 'Tau'),
    tauAssociationCone = cms.double(0),
    tauUnbiasCone = cms.double(1.2),
    PixelTracksSources = cms.VInputTag('hltPixelTracks'),
    ExtrapolationConeSize = cms.double(1),
    PixelIsolationConeSizeAtEC = cms.double(40),
    L1GTSeedLabel = cms.InputTag('hltL1sIsoTrack'),
    MaxVtxDXYSeed = cms.double(101),
    MaxVtxDXYIsol = cms.double(101),
    VertexLabel = cms.InputTag('hltTrimmedPixelVertices'),
    MagFieldRecordName = cms.string('VolumeBasedMagneticField'),
    minPTrack = cms.double(5),
    maxPTrackForIsolation = cms.double(3),
    EBEtaBoundary = cms.double(1.479),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
