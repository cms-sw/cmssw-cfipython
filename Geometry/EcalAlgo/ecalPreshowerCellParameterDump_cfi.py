import FWCore.ParameterSet.Config as cms

ecalPreshowerCellParameterDump = cms.EDAnalyzer('EcalPreshowerCellParameterDump',
  debug = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
