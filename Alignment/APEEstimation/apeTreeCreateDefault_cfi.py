import FWCore.ParameterSet.Config as cms

apeTreeCreateDefault = cms.EDAnalyzer('ApeTreeCreateDefault',
  resultFile = cms.string('defaultAPE.root')
)
