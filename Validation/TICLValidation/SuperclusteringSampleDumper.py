import FWCore.ParameterSet.Config as cms

def SuperclusteringSampleDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('SuperclusteringSampleDumper',
    tracksters = cms.InputTag('ticlTrackstersCLUE3DHigh'),
    recoToSimAssociatorCP = cms.InputTag('tracksterSimTracksterAssociationLinkingbyCLUE3D', 'recoToSim'),
    dnnInputsVersion = cms.string('v3'),
    deltaEtaWindow = cms.float(0.2),
    deltaPhiWindow = cms.float(0.7),
    seedPtThreshold = cms.float(3),
    candidateEnergyThreshold = cms.float(1.5),
    explVarRatioCut_energyBoundary = cms.float(50),
    explVarRatioMinimum_lowEnergy = cms.float(0.85),
    explVarRatioMinimum_highEnergy = cms.float(0.9),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
