import FWCore.ParameterSet.Config as cms

def CTPPSProtonReconstructionEfficiencyEstimatorMC(**kwargs):
  mod = cms.EDAnalyzer('CTPPSProtonReconstructionEfficiencyEstimatorMC',
    tagTracks = cms.InputTag(''),
    tagRecoProtonsMultiRP = cms.InputTag(''),
    lhcInfoLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False),
    rpId_45_N = cms.uint32(0),
    rpId_45_F = cms.uint32(0),
    rpId_56_N = cms.uint32(0),
    rpId_56_F = cms.uint32(0),
    outputFile = cms.string('output.root'),
    verbosity = cms.untracked.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
