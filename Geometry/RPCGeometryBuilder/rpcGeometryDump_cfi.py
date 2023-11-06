import FWCore.ParameterSet.Config as cms

rpcGeometryDump = cms.EDAnalyzer('RPCGeometryDump',
  verbose = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
