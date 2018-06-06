import FWCore.ParameterSet.Config as cms

hltElectronMissingHitsFilter = cms.EDFilter('HLTElectronMissingHitsFilter',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('hltSingleElectronOneOEMinusOneOPFilter'),
  electronProducer = cms.InputTag('hltL1NonIsoHLTNonIsoSingleElectronEt15LTIPixelMatchFilte'),
  barrelcut = cms.int32(0),
  endcapcut = cms.int32(0),
  ncandcut = cms.int32(1)
)
