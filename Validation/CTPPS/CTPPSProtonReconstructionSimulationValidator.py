import FWCore.ParameterSet.Config as cms

def CTPPSProtonReconstructionSimulationValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSProtonReconstructionSimulationValidator',
    lhcInfoLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False),
    tagHepMCBeforeSmearing = cms.InputTag('generator', 'unsmeared'),
    tagHepMCAfterSmearing = cms.InputTag('beamDivergenceVtxGenerator'),
    tagRecoProtonsSingleRP = cms.InputTag('ctppsProtons', 'singleRP'),
    tagRecoProtonsMultiRP = cms.InputTag('ctppsProtons', 'multiRP'),
    outputFile = cms.string('output.root'),
    verbosity = cms.untracked.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
