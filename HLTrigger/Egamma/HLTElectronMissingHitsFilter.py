import FWCore.ParameterSet.Config as cms

def HLTElectronMissingHitsFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTElectronMissingHitsFilter',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('hltSingleElectronOneOEMinusOneOPFilter'),
    electronProducer = cms.InputTag('hltL1NonIsoHLTNonIsoSingleElectronEt15LTIPixelMatchFilte'),
    barrelcut = cms.int32(0),
    endcapcut = cms.int32(0),
    ncandcut = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
