import FWCore.ParameterSet.Config as cms

hltElectronEoverpFilter = cms.EDFilter('HLTElectronEoverpFilterRegional',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('hltElectronPixelMatchFilter'),
  electronIsolatedProducer = cms.InputTag('pixelMatchElectronsForHLT'),
  electronNonIsolatedProducer = cms.InputTag('pixelMatchElectronsForHLT'),
  eoverpbarrelcut = cms.double(1.5),
  eoverpendcapcut = cms.double(2.45),
  ncandcut = cms.int32(1),
  doIsolated = cms.bool(True)
)
