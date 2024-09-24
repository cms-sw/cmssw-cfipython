import FWCore.ParameterSet.Config as cms

def SuperclusteringSampleDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('SuperclusteringSampleDumper',
    tracksters = cms.InputTag('ticlTrackstersCLUE3DHigh'),
    recoToSimAssociatorCP = cms.InputTag('tracksterSimTracksterAssociationLinkingbyCLUE3D', 'recoToSim'),
    dnnInputsVersion = cms.string('v2'),
    deltaEtaWindow = cms.double(0.2),
    deltaPhiWindow = cms.double(0.7),
    seedPtThreshold = cms.double(3),
    candidateEnergyThreshold = cms.double(1.5),
    explVarRatioCut_energyBoundary = cms.double(50),
    explVarRatioMinimum_lowEnergy = cms.double(0.85),
    explVarRatioMinimum_highEnergy = cms.double(0.9),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
