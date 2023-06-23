import FWCore.ParameterSet.Config as cms

totemDAQMappingESSourceXML = cms.ESSource('TotemDAQMappingESSourceXML',
  verbosity = cms.untracked.uint32(0),
  subSystem = cms.untracked.string(''),
  sampicSubDetId = cms.required.uint32,
  multipleChannelsPerPayload = cms.bool(False),
  configuration = cms.VPSet(
    cms.PSet(
      mappingFileNames = cms.vstring(),
      maskFileNames = cms.vstring(),
      validityRange = cms.EventRange('1:1-1:18446744073709551615')
    )
  ),
  appendToDataLabel = cms.string('')
)