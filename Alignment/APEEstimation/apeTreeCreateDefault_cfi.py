import FWCore.ParameterSet.Config as cms

apeTreeCreateDefault = cms.EDAnalyzer('ApeTreeCreateDefault',
  resultFile = cms.string('defaultAPE.root'),
  trackerTreeFile = cms.required.string,
  sectors = cms.required.VPSet,
  mightGet = cms.optional.untracked.vstring
)
