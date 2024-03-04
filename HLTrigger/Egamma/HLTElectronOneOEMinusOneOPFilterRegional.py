import FWCore.ParameterSet.Config as cms

def HLTElectronOneOEMinusOneOPFilterRegional(**kwargs):
  mod = cms.EDFilter('HLTElectronOneOEMinusOneOPFilterRegional',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('hltL1NonIsoHLTNonIsoSingleElectronEt15LTIPixelMatchFilter'),
    electronIsolatedProducer = cms.InputTag('hltPixelMatchElectronsL1Iso'),
    electronNonIsolatedProducer = cms.InputTag('hltPixelMatchElectronsL1NonIso'),
    barrelcut = cms.double(999.9),
    endcapcut = cms.double(999.9),
    ncandcut = cms.int32(1),
    doIsolated = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
