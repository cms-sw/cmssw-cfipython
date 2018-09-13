import FWCore.ParameterSet.Config as cms

hltElectronEtFilter = cms.EDFilter('HLTElectronEtFilter',
  saveTags = cms.bool(False),
  candTag = cms.InputTag('hltElectronPixelMatchFilter'),
  EtCutEB = cms.double(0),
  EtCutEE = cms.double(0),
  ncandcut = cms.int32(1),
  doIsolated = cms.bool(True)
)
