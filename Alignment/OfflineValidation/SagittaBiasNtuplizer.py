import FWCore.ParameterSet.Config as cms

def SagittaBiasNtuplizer(*args, **kwargs):
  mod = cms.EDAnalyzer('SagittaBiasNtuplizer',
    useReco = cms.bool(True),
    muons = cms.InputTag('muons'),
    doGen = cms.bool(False),
    genParticles = cms.InputTag('genParticles'),
    tracks = cms.InputTag('generalTracks'),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    muonEtaCut = cms.double(2.5),
    muonPtCut = cms.double(12),
    muondxySigCut = cms.double(4),
    minMassWindowCut = cms.double(70),
    maxMassWindowCut = cms.double(110),
    d0CompatibilityCut = cms.double(0.01),
    z0CompatibilityCut = cms.double(0.06),
    pTThresholds = cms.vdouble(
      30,
      10
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
