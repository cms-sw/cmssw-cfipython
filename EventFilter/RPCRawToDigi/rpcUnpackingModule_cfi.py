import FWCore.ParameterSet.Config as cms

rpcUnpackingModule = cms.EDProducer('RPCUnpackingModule',
  InputLabel = cms.InputTag('rawDataCollector'),
  doSynchro = cms.bool(True)
)
