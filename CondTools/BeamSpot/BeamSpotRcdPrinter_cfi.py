import FWCore.ParameterSet.Config as cms

BeamSpotRcdPrinter = cms.EDAnalyzer('BeamSpotRcdPrinter',
  conditionDatabase = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
  tagName = cms.string('BeamSpotObjects_PCL_byLumi_v0_prompt'),
  startIOV = cms.uint64(1406859487478481),
  endIOV = cms.uint64(1406876667347162),
  output = cms.string('summary.txt'),
  verbose = cms.bool(True),
  connect = cms.string(''),
  DBParameters = cms.PSet(
    authenticationPath = cms.untracked.string(''),
    authenticationSystem = cms.untracked.int32(0),
    security = cms.untracked.string(''),
    messageLevel = cms.untracked.int32(0)
  ),
  mightGet = cms.optional.untracked.vstring
)
