import FWCore.ParameterSet.Config as cms

rpcDigiMerger = cms.EDProducer('RPCDigiMerger',
  inputTagTwinMuxDigis = cms.InputTag('rpcTwinMuxRawToDigi'),
  inputTagOMTFDigis = cms.InputTag('omtfStage2Digis'),
  inputTagCPPFDigis = cms.InputTag('rpcCPPFRawToDigi'),
  mightGet = cms.optional.untracked.vstring
)
