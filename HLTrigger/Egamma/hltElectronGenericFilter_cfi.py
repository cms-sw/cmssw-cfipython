import FWCore.ParameterSet.Config as cms

hltElectronGenericFilter = cms.EDFilter('HLTElectronGenericFilter',
  saveTags = cms.bool(False),
  candTag = cms.InputTag('hltSingleElectronOneOEMinusOneOPFilter'),
  isoTag = cms.InputTag('hltSingleElectronTrackIsol'),
  nonIsoTag = cms.InputTag('hltSingleElectronHcalTrackIsol'),
  lessThan = cms.bool(True),
  thrRegularEB = cms.double(0),
  thrRegularEE = cms.double(0),
  thrOverPtEB = cms.double(-1),
  thrOverPtEE = cms.double(-1),
  thrTimesPtEB = cms.double(-1),
  thrTimesPtEE = cms.double(-1),
  ncandcut = cms.int32(1),
  doIsolated = cms.bool(True),
  L1IsoCand = cms.InputTag('hltPixelMatchElectronsL1Iso'),
  L1NonIsoCand = cms.InputTag('hltPixelMatchElectronsL1NonIso')
)
