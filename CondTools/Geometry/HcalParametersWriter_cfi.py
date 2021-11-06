import FWCore.ParameterSet.Config as cms

HcalParametersWriter = cms.EDAnalyzer('HcalParametersDBBuilder',
  fromDD4hep = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
