import FWCore.ParameterSet.Config as cms

def HLTElectronMissingHitsFilter(**kwargs):
  mod = cms.EDFilter('HLTElectronMissingHitsFilter',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('hltSingleElectronOneOEMinusOneOPFilter'),
    electronProducer = cms.InputTag('hltL1NonIsoHLTNonIsoSingleElectronEt15LTIPixelMatchFilte'),
    barrelcut = cms.int32(0),
    endcapcut = cms.int32(0),
    ncandcut = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
